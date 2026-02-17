# claude_apify_integration.py

import requests

class ClaudeApifyIntegration:
    def __init__(self, claude_api_key, apify_api_key):
        self.claude_api_key = claude_api_key
        self.apify_api_key = apify_api_key

    def query_claude(self, prompt):
        headers = {'Authorization': f'Bearer {self.claude_api_key}', 'Content-Type': 'application/json'}
        json_data = {'prompt': prompt}
        response = requests.post('https://api.claude.ai/v1/queries', headers=headers, json=json_data)
        return response.json()

    def launch_apify_actor(self, actor_id, input_data):
        url = f'https://api.apify.com/v2/actor-tasks/{actor_id}/run-sync
        params = {'token': self.apify_api_key}
        response = requests.post(url, params=params, json=input_data)
        return response.json()

# Example usage:
# integration = ClaudeApifyIntegration('your_claude_api_key', 'your_apify_api_key')
# claude_response = integration.query_claude('What is the weather today?')
# apify_response = integration.launch_apify_actor('your_actor_id', {'key': 'value'})