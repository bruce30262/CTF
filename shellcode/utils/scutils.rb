#!/usr/bin/env ruby

# utils for shellcode

$stderr.sync = true
require 'optparse'

def getshellcode(filename)
    resp = `nasm -f bin -o code.o #{filename} && xxd -i code.o`
    if resp.include?"0x00"
        puts "Null byte alert!"
    end
    puts resp
    sc_hex = ""
    open("code.o", "rb") do |file|
        while( c = file.read(1) ) do
            sc_hex += "\\x%02x" % c.ord
        end
    end
    puts "hex string: \"#{sc_hex}\""
    `rm code.o`
end

# default options
filename = nil
asm_opt = nil
sc_opt = false
outfile = "a.bin"

# parse arguments
file = __FILE__
ARGV.options do |opts|
    opts.banner = "A simple x86 & x64 shellcode utility by bruce30262\n"
    opts.banner += "Usage: #{file} [options] [param]"
   
    opts.on("-f", "--file=val", "the assembly file ( ex. --file=shell.s )") { |val| filename = val }
    opts.on("-a", "--asm=val [ 32 or 64 ]", "assemble assembly file into x86 or x64 binary") { |val| asm_opt = val }
    opts.on("-o", "--out=val", "output binary name after assembling the assembly ( default = a.bin )") { |val| outfile = val }
    opts.on("-s", "--sc", "--shellcode", "generate shellcode hex string ( ex. myshellcode = \"\\xcd\\x80\" )")   { sc_opt = true }
    opts.on("-h", "--help", "Display this message")         { puts opts; exit 0 }

    OPT = opts
    opts.parse!
end

if filename.nil?
    puts "No asm filename selected. Use the -h or --help to check the usage."
else
    if File.exists?(filename)
        if asm_opt.nil?
            if sc_opt == false
                puts "No option selected. Use the -h or --help to check the usage."
                exit -1
            end
        elsif asm_opt == "32"
            resp = `nasm -f elf32 -o #{filename}.o #{filename} && ld -m elf_i386 -o #{outfile} #{filename}.o && rm -f #{filename}.o`
            puts "output binary: #{outfile}"
        elsif asm_opt == "64"
            resp = `nasm -f elf64 -o #{filename}.o #{filename} && ld -m elf_x86_64 -o #{outfile} #{filename}.o && rm -f #{filename}.o`
            puts "output binary: #{outfile}"
        else
            puts "Wrong asm option: #{asm_opt} ( must be \"32\" or \"64\" )"
            exit -1
        end

        if sc_opt == true
            getshellcode(filename)
        end
    else
        puts "No file exist: #{filename}"
    end
end


