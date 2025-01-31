# Copyright 2017-2020 Palantir Technologies, Inc.
# Copyright 2021- Python Language Server Contributors.

"""Some Language Server Protocol constants.

https://github.com/Microsoft/language-server-protocol/blob/master/protocol.md
"""
from __future__ import annotations

from enum import Enum
from typing import Optional, TypedDict


class CompletionItemKind:
    Text = 1
    Method = 2
    Function = 3
    Constructor = 4
    Field = 5
    Variable = 6
    Class = 7
    Interface = 8
    Module = 9
    Property = 10
    Unit = 11
    Value = 12
    Enum = 13
    Keyword = 14
    Snippet = 15
    Color = 16
    File = 17
    Reference = 18
    Folder = 19
    EnumMember = 20
    Constant = 21
    Struct = 22
    Event = 23
    Operator = 24
    TypeParameter = 25


class DocumentHighlightKind:
    Text = 1
    Read = 2
    Write = 3


class DiagnosticSeverity(int, Enum):
    Error = 1
    Warning = 2
    Information = 3
    Hint = 4


class DiagnosticTag(int, Enum):
    Unnecessary = 1
    Deprecated = 2


class InsertTextFormat:
    PlainText = 1
    Snippet = 2


class MessageType:
    Error = 1
    Warning = 2
    Info = 3
    Log = 4


class SymbolKind:
    File = 1
    Module = 2
    Namespace = 3
    Package = 4
    Class = 5
    Method = 6
    Property = 7
    Field = 8
    Constructor = 9
    Enum = 10
    Interface = 11
    Function = 12
    Variable = 13
    Constant = 14
    String = 15
    Number = 16
    Boolean = 17
    Array = 18


class TextDocumentSyncKind:
    NONE = 0
    FULL = 1
    INCREMENTAL = 2


class NotebookCellKind:
    Markup = 1
    Code = 2


# https://microsoft.github.io/language-server-protocol/specifications/lsp/3.17/specification/#errorCodes
class ErrorCodes:
    ParseError = -32700
    InvalidRequest = -32600
    MethodNotFound = -32601
    InvalidParams = -32602
    InternalError = -32603
    jsonrpcReservedErrorRangeStart = -32099
    ServerNotInitialized = -32002
    UnknownErrorCode = -32001
    jsonrpcReservedErrorRangeEnd = -32000
    lspReservedErrorRangeStart = -32899
    ServerCancelled = -32802
    ContentModified = -32801
    RequestCancelled = -32800
    lspReservedErrorRangeEnd = -32800


class Position(TypedDict):
    """Position in a text document expressed as zero-based line and character offset.

    A position is between two characters like an 'insert' cursor in a editor.
    Special values like for example (-1,-1) which indicates that the position
    is invalid.
    """

    line: int
    character: int

class Range(TypedDict):
    """The range type represents a span of text in the document."""

    start: Position
    end: Position

class Diagnostic(TypedDict):
    """The type of a diagnostic the lsp should publish."""

    source: str
    range: Range
    message: str
    severity: DiagnosticSeverity
    code: str
    tags: list[DiagnosticTag]
