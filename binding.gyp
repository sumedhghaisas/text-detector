{
    "targets": [
        {
            "target_name": "textdetector",
            "dependencies": [
                "native/ocr/ocr.gyp:ocr",
                "deps/leptonica/leptonica.gyp:liblept",
                "deps/jpg/jpg.gyp:jpg",
                "deps/lodepng/lodepng.gyp:lodepng",
                "deps/tesseract/tesseract.gyp:libtesseract",
                "deps/zxing/zxing.gyp:libzxing",
                "deps/lswms/lswms.gyp:liblswms",
            ],
            "include_dirs": [
                "<!(node -e \"require('nan')\")",
                "native",
                "deps/jpg",
                "deps/lodepng",
                "deps/leptonica/src",
                "deps/tesseract/api",
                "deps/tesseract/ccmain",
                "deps/tesseract/ccutil",
                "deps/tesseract/classify",
                "deps/tesseract/cutil",
                "deps/tesseract/dict",
                "deps/tesseract/image",
                "deps/tesseract/textwork",
                "deps/tesseract/viewer",
                "deps/tesseract/wordrec",
                "deps/zxing/core/src",
                "deps/opencv/include",
                "deps/opencv/modules/core/include",
                "deps/opencv/modules/dynamicuda/include",
                "deps/opencv/modules/imgproc/include",
	        "deps/opencv/modules/text/include",
	        "deps/opencv/modules/text/include",
                "deps/lswms",
	    ],
            "sources": [
                "native/index.cc",
                "native/async.cc",
                "native/sync.cc"
            ]
        }
    ]
}
