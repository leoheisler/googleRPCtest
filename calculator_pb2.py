# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# NO CHECKED-IN PROTOBUF GENCODE
# source: calculator.proto
# Protobuf Python Version: 5.27.2
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import runtime_version as _runtime_version
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_runtime_version.ValidateProtobufRuntimeVersion(
    _runtime_version.Domain.PUBLIC,
    5,
    27,
    2,
    '',
    'calculator.proto'
)
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x10\x63\x61lculator.proto\"\"\n\nSumRequest\x12\t\n\x01\x61\x18\x01 \x01(\x01\x12\t\n\x01\x62\x18\x02 \x01(\x01\"\x15\n\x08SumReply\x12\t\n\x01s\x18\x01 \x01(\x01\"\'\n\x0fMultiplyRequest\x12\t\n\x01\x61\x18\x01 \x01(\x01\x12\t\n\x01\x62\x18\x02 \x01(\x01\"\x1a\n\rMultiplyReply\x12\t\n\x01s\x18\x01 \x01(\x01\"1\n\x0e\x42iggestRequest\x12\t\n\x01\x61\x18\x01 \x01(\x01\x12\t\n\x01\x62\x18\x02 \x01(\x01\x12\t\n\x01\x63\x18\x03 \x01(\x01\"\x19\n\x0c\x42iggestReply\x12\t\n\x01s\x18\x01 \x01(\x01\"0\n\nDivRequest\x12\x11\n\tdividendo\x18\x01 \x01(\x01\x12\x0f\n\x07\x64ivisor\x18\x02 \x01(\x01\")\n\x08\x44ivReply\x12\x0b\n\x03quo\x18\x01 \x01(\x01\x12\x10\n\x08\x64iv_rest\x18\x02 \x01(\x01\x32\xa3\x01\n\nCalculator\x12\x1d\n\x03Sum\x12\x0b.SumRequest\x1a\t.SumReply\x12,\n\x08Multiply\x12\x10.MultiplyRequest\x1a\x0e.MultiplyReply\x12)\n\x07\x42iggest\x12\x0f.BiggestRequest\x1a\r.BiggestReply\x12\x1d\n\x03\x44iv\x12\x0b.DivRequest\x1a\t.DivReplyb\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'calculator_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
  DESCRIPTOR._loaded_options = None
  _globals['_SUMREQUEST']._serialized_start=20
  _globals['_SUMREQUEST']._serialized_end=54
  _globals['_SUMREPLY']._serialized_start=56
  _globals['_SUMREPLY']._serialized_end=77
  _globals['_MULTIPLYREQUEST']._serialized_start=79
  _globals['_MULTIPLYREQUEST']._serialized_end=118
  _globals['_MULTIPLYREPLY']._serialized_start=120
  _globals['_MULTIPLYREPLY']._serialized_end=146
  _globals['_BIGGESTREQUEST']._serialized_start=148
  _globals['_BIGGESTREQUEST']._serialized_end=197
  _globals['_BIGGESTREPLY']._serialized_start=199
  _globals['_BIGGESTREPLY']._serialized_end=224
  _globals['_DIVREQUEST']._serialized_start=226
  _globals['_DIVREQUEST']._serialized_end=274
  _globals['_DIVREPLY']._serialized_start=276
  _globals['_DIVREPLY']._serialized_end=317
  _globals['_CALCULATOR']._serialized_start=320
  _globals['_CALCULATOR']._serialized_end=483
# @@protoc_insertion_point(module_scope)
