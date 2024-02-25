# Роман Гулаков, 13-я когорта — Финальный проект. Инженер по тестированию плюс

import sender_stand_request


def test_track_info():
    track = sender_stand_request.track_number_order()
    result = sender_stand_request.get_track_number(track)
    assert result.status_code == 200
