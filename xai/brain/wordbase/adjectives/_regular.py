

#calss header
class _REGULAR():
	def __init__(self,): 
		self.name = "REGULAR"
		self.definitions = [u'happening or doing something often: ', u'existing or happening repeatedly in a fixed pattern, with equal or similar amounts of space or time between one and the next; even: ', u'Someone who is regular empties their bowels often enough, and a woman who is regular always has her period at approximately the same time: ', u'usual or ordinary: ', u'A regular verb, noun, or adjective follows the usual rules in the structure of its various forms: ', u'a normal man who is liked and trusted', u'an army that exists all the time, or a soldier in such an army', u'the same on both or all sides: ', u'real; complete: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
