require 'rubygems'
require 'securerandom.rb'

class ArgError < RuntimeError
end

@netlist = ""
@part_count = 0

def uid
	count = @part_count
	@part_count += 1

	return "c_#{count}"
end

def part(type, a, b = nil)
	if a.class == String and b.class == Array then
		name = a
		args = b
	elsif a.class == Array then
		name = uid
		args = a
	else
		raise ArgError
	end

	out = "X#{name} #{args.join(' ')} #{type}"
	@netlist += out + "\n"
end

part 'beta', 'my_beta', ['a', 'b']
part 'mosfet', ['a', 'b']
puts @netlist
