{
  'includes': [ '../common.gyp' ],
  'targets': [
    {
      'target_name': 'libopencv',
      'type': 'static_library',
      'include_dirs': [
        './include',
        './modules/core/include',
        './modules/dynamicuda/include',
        './modules/imgproc/include',
      ],
      'sources': [
        'modules/core/src/algorithm.cpp',
        'modules/core/src/alloc.cpp',
        'modules/core/src/arithm1.cpp',
        'modules/core/src/array.cpp',
        'modules/core/src/cmdparser.cpp',
        'modules/core/src/convert.cpp',
        'modules/core/src/copy.cpp',
        'modules/core/src/datastructs.cpp',
        'modules/core/src/drawing.cpp',
        'modules/core/src/dxt.cpp',
        'modules/core/src/gl_core_3_1.cpp',
        'modules/core/src/glob.cpp',
        'modules/core/src/gpumat.cpp',
        'modules/core/src/lapack.cpp',
        'modules/core/src/mathfuncs.cpp',
        'modules/core/src/matmul.cpp',
        'modules/core/src/matop.cpp',
        'modules/core/src/matrix.cpp',
        'modules/core/src/opengl_interop.cpp',
        'modules/core/src/opengl_interop_deprecated.cpp',
        'modules/core/src/out.cpp',
        'modules/core/src/parallel.cpp',
        'modules/core/src/persistence.cpp',
        'modules/core/src/rand.cpp',
        'modules/core/src/stat.cpp',
        'modules/core/src/system.cpp',
        'modules/core/src/tables1.cpp',
        'modules/dynamicuda/src/main.cpp',
        'modules/imgproc/src/accum.cpp',
        'modules/imgproc/src/approx.cpp',
        'modules/imgproc/src/canny.cpp',
        'modules/imgproc/src/clahe.cpp',
        'modules/imgproc/src/color1.cpp',
        'modules/imgproc/src/contours.cpp',
        'modules/imgproc/src/convhull.cpp',
        'modules/imgproc/src/corner.cpp',
        'modules/imgproc/src/cornersubpix.cpp',
        'modules/imgproc/src/deriv.cpp',
        'modules/imgproc/src/distransform.cpp',
        'modules/imgproc/src/emd.cpp',
        'modules/imgproc/src/featureselect.cpp',
        'modules/imgproc/src/filter.cpp',
        'modules/imgproc/src/floodfill.cpp',
        'modules/imgproc/src/gabor.cpp',
        'modules/imgproc/src/generalized_hough.cpp',
        'modules/imgproc/src/geometry.cpp',
        'modules/imgproc/src/grabcut.cpp',
        'modules/imgproc/src/histogram.cpp',
        'modules/imgproc/src/hough.cpp',
        'modules/imgproc/src/imgwarp.cpp',
        'modules/imgproc/src/linefit.cpp',
        'modules/imgproc/src/matchcontours.cpp',
        'modules/imgproc/src/moments.cpp',
        'modules/imgproc/src/morph.cpp',
        'modules/imgproc/src/phasecorr.cpp',
        'modules/imgproc/src/pyramids1.cpp',
        'modules/imgproc/src/rotcalipers.cpp',
        'modules/imgproc/src/samplers.cpp',
        'modules/imgproc/src/segmentation.cpp',
        'modules/imgproc/src/shapedescr.cpp',
        'modules/imgproc/src/smooth.cpp',
        'modules/imgproc/src/subdivision2d.cpp',
        'modules/imgproc/src/sumpixels.cpp',
        'modules/imgproc/src/tables2.cpp',
        'modules/imgproc/src/templmatch.cpp',
        'modules/imgproc/src/thresh.cpp',
        'modules/imgproc/src/undistort.cpp',
        'modules/imgproc/src/utils.cpp',
	'modules/text/src/erfilter.cpp',
	'modules/text/src/ocr_beamsearch_decoder.cpp',
	'modules/text/src/ocr_hmm_decoder.cpp',
	'modules/text/src/ocr_tesseract.cpp',
	'modules/ml/src/ann.mlp.cpp',
        'modules/ml/src/boost.cpp',
	 'modules/ml/src/data.cpp',
	 'modules/ml/src/em.cpp',
        "modules/ml/src/gbt.cpp",
        "modules/ml/src/inner_functions.cpp",
        "modules/ml/src/kdtree.cpp",
        "modules/ml/src/knearest.cpp",
        "modules/ml/src/lr.cpp",
        "modules/ml/src/nbayes.cpp",
        "modules/ml/src/rtrees.cpp",
        "modules/ml/src/svm.cpp",
        "modules/ml/src/testset.cpp",
        "modules/ml/src/tree.cpp"
	],
    },
  ]
}
