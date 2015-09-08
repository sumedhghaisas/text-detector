{
    "targets": [
        {
            "target_name": "textdetector",
            "dependencies": [
                "native/ocr/ocr.gyp:ocr",
                "deps/leptonica/leptonica.gyp:liblept"
            ],
            "include_dirs": [
                "<!(node -e \"require('nan')\")",
                "native"
            ],
            "sources": [
                "native/index.cc",
                "native/async.cc",
                "native/sync.cc"
            ]
        }
    ]
}
