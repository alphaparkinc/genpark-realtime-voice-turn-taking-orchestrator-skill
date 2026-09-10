from client import RealtimeVoiceTurnTakingOrchestratorClient

def main():
    client = RealtimeVoiceTurnTakingOrchestratorClient()
    res = client.orchestrate_voice_turn()
    print('Realtime Voice Turn Taking: ' + res['orchestration_id'] + ' (' + res['turn_action'] + ')')
    print('Barge-in Detected: ' + str(res['acoustic_barge_in_detected']) + ' | Buffer Action: ' + res['buffer_action'])
    print('Latency Budget: ' + str(res['latency_budget_ms']) + 'ms | Telemetry: ' + res['session_telemetry_url'])

if __name__ == '__main__':
    main()
