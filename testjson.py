output = {
    "archives": [
        {
            "command_line": [
                "/usr/local/bin/borg",
                "create",
                "-v",
                "--stats",
                "backup_cloud@10.100.1.100:/data/cloud::cloud-{now:%Y-%m-%d}",
                "/storage/data"
            ],
            "comment": "",
            "duration": 71.670957,
            "end": "2018-03-19T01:21:16.000000",
            "hostname": "GosNextCloud-01",
            "id": "7d4a82580446a2fad936c5129aeadc5d1eed37b7d90fa6d0418d0fd96c98d1bb",
            "limits": {
                "max_archive_size": 0.0013216521352642796
            },
            "name": "cloud-2018-03-19",
            "start": "2018-03-19T01:20:04.000000",
            "stats": {
                "compressed_size": 410658946450,
                "deduplicated_size": 44189314,
                "nfiles": 245764,
                "original_size": 457811633702
            },
            "username": "root"
        }
    ],
    "cache": {
        "path": "/root/.cache/borg/b7a60649bca88b02261b3f0848647b04bc174d6ad91478d7973bab79d2d74af1",
        "stats": {
            "total_chunks": 2418045,
            "total_csize": 2452403860822,
            "total_size": 2733990077184,
            "total_unique_chunks": 201274,
            "unique_csize": 188036157669,
            "unique_size": 209834329032
        }
    },
    "encryption": {
        "mode": "none"
    },
    "repository": {
        "id": "b7a60649bca88b02261b3f0848647b04bc174d6ad91478d7973bab79d2d74af1",
        "last_modified": "2018-03-19T01:21:16.000000",
        "location": "/data/cloud"
    }
}