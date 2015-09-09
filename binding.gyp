{
    "targets": [
        {
            "target_name": "textdetector",
            "dependencies": [
                "native/ocr/ocr.gyp:ocr",
                "deps/leptonica/leptonica.gyp:liblept",
                "deps/jpg/jpg.gyp:jpg",
                "deps/lodepng/lodepng.gyp:lodepng",
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
