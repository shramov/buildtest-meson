project('buildtest', 'c', 'cpp'
	, version: '0.0.0'
	, default_options : ['cpp_std=c++17', 'werror=true', 'optimization=2']
	, meson_version: '>= 0.53'
	)

fmt = dependency('fmt')

shared_library('buildtest', ['src/buildtest.cc'],
                include_directories: ['src'],
                dependencies : [fmt],
                version: '0', soversion: '0',
                install : true)
