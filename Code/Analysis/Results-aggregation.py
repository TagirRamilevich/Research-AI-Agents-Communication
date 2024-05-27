import pandas as pd
import os

def prepare_dataframe(exp_num):
    file_path = f'/content/drive/My Drive/HSE Agents RL/Experiments/Exp_{exp_num}'
    
    history_dfs = []
    results_dfs = []
    
    counter = 1

    for file_name in os.listdir(file_path):
        full_file_path = os.path.join(file_path, file_name)
        
        if file_name.endswith('_df_history.csv'):
            df = pd.read_csv(full_file_path)
            df = df.drop('Unnamed: 0', axis=1)
            df['exp'] = counter
            history_dfs.append(df)
        
        elif file_name.endswith('_df_results.csv'):
            df = pd.read_csv(full_file_path)
            df = df.drop('Unnamed: 0', axis=1)
            df['exp'] = counter
            counter += 1
            results_dfs.append(df)

    combined_history_df = pd.concat(history_dfs, ignore_index=True)
    combined_results_df = pd.concat(results_dfs, ignore_index=True)

    combined_history_df.to_csv(os.path.join(file_path, f'Results/exp_{exp_num}_combined_history.csv'), index=False)
    combined_results_df.to_csv(os.path.join(file_path, f'Results/exp_{exp_num}_combined_results.csv'), index=False)

    def ensure_30_rounds(df):
        """Ensure each experiment has at least 30 rounds by adding missing rounds with default values."""
        updated_dfs = []
        for exp in df['exp'].unique():
            exp_df = df[df['exp'] == exp]
            total_rounds = exp_df['attempts'].sum()
            if total_rounds < 30:
                missing_rounds = 30 - total_rounds
                new_rows = pd.DataFrame({
                    'arm': [0] * missing_rounds,
                    'attempts': [1] * missing_rounds,
                    'reward': [0] * missing_rounds,
                    'success_rate': [0] * missing_rounds,
                    'exp': [exp] * missing_rounds
                })
                exp_df = pd.concat([exp_df, new_rows], ignore_index=True)
            updated_dfs.append(exp_df)
        return pd.concat(updated_dfs, ignore_index=True)

    combined_results_df = ensure_30_rounds(combined_results_df)

    def aggregate_results(df):
        """Aggregate results by experiment, calculating total rounds, total reward, total regret, and average reward."""
        grouped = df.groupby('exp').agg(
            total_rounds=pd.NamedAgg(column='attempts', aggfunc='sum'),
            total_reward=pd.NamedAgg(column='reward', aggfunc='sum')
        )
        grouped['total_regret'] = grouped['total_rounds'] - grouped['total_reward']
        grouped['average_reward'] = round(grouped['total_reward'] / grouped['total_rounds'], 2)
        return grouped

    aggregated_results_df = aggregate_results(combined_results_df)

    best_handle_prob = combined_history_df.groupby('exp')['best_handle_probability'].sum().reset_index()
    aggregated_results_df = aggregated_results_df.merge(best_handle_prob, on='exp', how='left')
    aggregated_results_df['best_handle_probability'] = round(aggregated_results_df['best_handle_probability'] / aggregated_results_df['total_rounds'], 2)
    aggregated_results_df['best_handle_probability'] = aggregated_results_df['best_handle_probability'].fillna(0)

    aggregated_results_df.to_csv(os.path.join(file_path, f'Results/exp_{exp_num}_aggregated_results.csv'), index=False)
