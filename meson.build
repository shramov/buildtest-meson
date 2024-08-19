project('buildtest', 'c', 'cpp'
	, version: '0.0.0'
	, default_options : ['cpp_std=c++17', 'werror=true', 'optimization=2']
	, meson_version: '>= 0.53'
	)

fmt = dependency('fmt')

link_args = []
if host_machine.system() == 'windows'
  link_args = ['-Wl,/DEF:@0@/@1@'.format(meson.current_source_dir(), 'src/buildtest.def')]
endif

shared_library('buildtest', ['src/buildtest.cc'],
                include_directories: ['src'],
                dependencies : [fmt],
                link_args: link_args,
                link_depends: 'src/buildtest.def',
                version: '0', soversion: '0',
                install : true)
