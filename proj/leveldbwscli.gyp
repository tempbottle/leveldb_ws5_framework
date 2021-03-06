{

	'targets': [
	{  
		'target_name': "wscli",
		'type':'executable',	
		 'includes':[
			'../deps/osconfig.gypi',
			'../proj/configd.gypi',
		],
		'dependencies': [
			'../deps/protobuf3.gyp:protobuf_full_do_not_use',
			'../deps/json2pb.gyp:json2pb',
			'../deps/jansson.gyp:jansson',		
			'../deps/glog.gyp:glog',
			'../deps/leveldb.gyp:leveldb',
			'../deps/str2argv.gyp:str2argv',
			'../deps/gflags.gyp:gflags',
		],
		'include_dirs': [
			'../deps/boost_1_57_0',
			'../deps/websocketpp-master',
			'../deps/protobuf3/src',
			'../deps/json2pb-master',
			'../deps/glog/src',
			'../deps/leveldb/include',
			'../deps/cstr2argv',
			'../src/proto',
			'../src/proto/model',
			'../src/util',
			'../src/db',

			],
		'sources': [ 
			'../src/leveldbwscli/leveldbdispatcher.cc',
			'../src/leveldbwscli/leveldbdispatcher.h',
			'../src/leveldbwscli/wscli.cc',
			'../src/leveldbwscli/wscli.h',
			'../src/leveldbwscli/wsclimain.cc',
			'../src/leveldbwscli/wsclimain.h',
			'../src/leveldbwscli/main.cc',
			'../src/util/msgdispatcher.hpp',
			'../src/util/codec.cc',
			'../src/util/codec.h',
			'../src/util/codecinmsg.cc',
			'../src/util/codecinmsg.h',
			'../src/util/glog.cc',
			'../src/util/glog.h',
			'../src/util/nodeexception.h',
			'../src/proto/packmsg.pb.cc',
			'../src/proto/packmsg.pb.h',
			'../src/proto/model/model_db.pb.cc',
			'../src/proto/model/model_db.pb.h',
			'../src/proto/model/model_comm.pb.cc',
			'../src/proto/model/model_comm.pb.h',
		],
		'conditions': [
			['OS=="win"', {
				'libraries': [
					'Advapi32.lib',
					'User32.lib'
				],
				'include_dirs': [
					'../deps/gflags/src/windows',
				 ]
			}]
		],
    }],
}	