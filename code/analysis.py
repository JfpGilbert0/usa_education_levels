import pandas as pd

# Load the dataset
file_path = "data/usa_00001.csv"
df = pd.read_csv(file_path)

# get state names
states_df = pd.read_csv("data/state_mapping.csv")
states_df['state'] = states_df['state'].str.strip()
# join datasets
df_with_states = pd.merge(df, states_df, on='STATEICP')

# Filter for respondents with a doctoral degree (verify the code for doctoral degree in the codebook)
doctoral_degree_only = df_with_states[df_with_states['EDUCD'] == 116]
# Group by state and count the number of respondents
state_doctoral_counts = doctoral_degree_only.groupby('state').size().reset_index(name='doctoral_count')
state_counts = df_with_states.groupby('state').size().reset_index(name='n')
# merge the two tables with counts
analysis_data = pd.merge(state_counts, state_doctoral_counts, on='state')
#Get ratio
analysis_data['ratio'] = analysis_data['doctoral_count']/ analysis_data['n']
# Display the result
print(analysis_data)

# Save the result to a CSV file
analysis_data.to_csv("data/analysis/doctoral_degree_by_state.csv", index=False)


