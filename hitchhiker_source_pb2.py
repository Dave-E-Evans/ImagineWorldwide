# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: hitchhiker_source.proto
# Protobuf Python Version: 4.25.0
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x17hitchhiker_source.proto\x12\x11hitchhiker_source\"T\n\x04\x46ile\x12\x0f\n\x07\x66ile_id\x18\x01 \x01(\t\x12\x11\n\tfile_name\x18\x02 \x01(\t\x12\x0c\n\x04type\x18\x03 \x01(\t\x12\x11\n\x04\x62lob\x18\x04 \x01(\x0cH\x00\x88\x01\x01\x42\x07\n\x05_blob\".\n\x08\x46ileList\x12\x0f\n\x07\x66ile_id\x18\x01 \x01(\t\x12\x11\n\tfile_name\x18\x02 \x01(\t\"\x14\n\x12GetSourceIdRequest\"%\n\x10GetSourceIdReply\x12\x11\n\tsource_id\x18\x01 \x01(\t\"@\n\x13GetDownloadsRequest\x12\x11\n\tclient_id\x18\x01 \x01(\t\x12\x16\n\x0e\x64\x65stination_id\x18\x02 \x01(\t\"C\n\x11GetDownloadsReply\x12.\n\tfile_list\x18\x01 \x03(\x0b\x32\x1b.hitchhiker_source.FileList\"X\n\x13\x44ownloadFileRequest\x12\x11\n\tclient_id\x18\x01 \x01(\t\x12.\n\tfile_list\x18\x02 \x03(\x0b\x32\x1b.hitchhiker_source.FileList\";\n\x11\x44ownloadFileReply\x12&\n\x05\x66iles\x18\x01 \x03(\x0b\x32\x17.hitchhiker_source.File\"q\n\x14MarkDeliveredRequest\x12\x11\n\tclient_id\x18\x01 \x01(\t\x12\x16\n\x0e\x64\x65stination_id\x18\x02 \x01(\t\x12.\n\tfile_list\x18\x03 \x03(\x0b\x32\x1b.hitchhiker_source.FileList\"\x14\n\x12MarkDeliveredReply2\x92\x03\n\x10HitchhikerSource\x12[\n\x0bGetSourceId\x12%.hitchhiker_source.GetSourceIdRequest\x1a#.hitchhiker_source.GetSourceIdReply\"\x00\x12^\n\x0cGetDownloads\x12&.hitchhiker_source.GetDownloadsRequest\x1a$.hitchhiker_source.GetDownloadsReply\"\x00\x12^\n\x0c\x44ownloadFile\x12&.hitchhiker_source.DownloadFileRequest\x1a$.hitchhiker_source.DownloadFileReply\"\x00\x12\x61\n\rMarkDelivered\x12\'.hitchhiker_source.MarkDeliveredRequest\x1a%.hitchhiker_source.MarkDeliveredReply\"\x00\x62\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'hitchhiker_source_pb2', _globals)
if _descriptor._USE_C_DESCRIPTORS == False:
  DESCRIPTOR._options = None
  _globals['_FILE']._serialized_start=46
  _globals['_FILE']._serialized_end=130
  _globals['_FILELIST']._serialized_start=132
  _globals['_FILELIST']._serialized_end=178
  _globals['_GETSOURCEIDREQUEST']._serialized_start=180
  _globals['_GETSOURCEIDREQUEST']._serialized_end=200
  _globals['_GETSOURCEIDREPLY']._serialized_start=202
  _globals['_GETSOURCEIDREPLY']._serialized_end=239
  _globals['_GETDOWNLOADSREQUEST']._serialized_start=241
  _globals['_GETDOWNLOADSREQUEST']._serialized_end=305
  _globals['_GETDOWNLOADSREPLY']._serialized_start=307
  _globals['_GETDOWNLOADSREPLY']._serialized_end=374
  _globals['_DOWNLOADFILEREQUEST']._serialized_start=376
  _globals['_DOWNLOADFILEREQUEST']._serialized_end=464
  _globals['_DOWNLOADFILEREPLY']._serialized_start=466
  _globals['_DOWNLOADFILEREPLY']._serialized_end=525
  _globals['_MARKDELIVEREDREQUEST']._serialized_start=527
  _globals['_MARKDELIVEREDREQUEST']._serialized_end=640
  _globals['_MARKDELIVEREDREPLY']._serialized_start=642
  _globals['_MARKDELIVEREDREPLY']._serialized_end=662
  _globals['_HITCHHIKERSOURCE']._serialized_start=665
  _globals['_HITCHHIKERSOURCE']._serialized_end=1067
# @@protoc_insertion_point(module_scope)
