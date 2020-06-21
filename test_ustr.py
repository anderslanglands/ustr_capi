from cffi import FFI

ffi = FFI()
ffi.cdef("""
    const char* ustr(const char* s);
    size_t ustr_len(const char* us);
    uint64_t ustr_hash(const char* us);
""")
lib = ffi.dlopen('libustr_capi.so')
s = 'The quick brown fox jumped over the lazy dog'.encode('utf-8')
us = lib.ustr(s)
ln = lib.ustr_len(us)
hash = lib.ustr_hash(us)
print('s len: %d' % len(s))
print(ffi.buffer(us, ln)[:].decode('utf-8'))
print('ln: %d' % ln)
print('hash: %x' % hash)
