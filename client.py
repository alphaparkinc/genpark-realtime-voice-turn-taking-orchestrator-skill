class RealtimeVoiceTurnTakingOrchestratorClient:
    def orchestrate_voice_turn(self, vad_energy_db=-18.4, silence_duration_ms=280, agent_speaking=True):
        turn_action = 'BARGE_IN_INTERRUPT' if (vad_energy_db > -22.0 and agent_speaking) else 'YIELD_TO_USER' if silence_duration_ms > 450 else 'CONTINUE_STREAMING'
        return {
            'orchestration_id': 'vtt_orch_4418',
            'vad_energy_db': vad_energy_db,
            'silence_duration_ms': silence_duration_ms,
            'turn_action': turn_action,
            'acoustic_barge_in_detected': (turn_action == 'BARGE_IN_INTERRUPT'),
            'latency_budget_ms': 65,
            'buffer_action': 'FLUSH_AUDIO_OUTPUT_QUEUE' if turn_action == 'BARGE_IN_INTERRUPT' else 'STREAM_AUDIO_CHUNKS',
            'session_telemetry_url': 'https://voice.realtime.genpark.ai/sessions/4418.json'
        }
