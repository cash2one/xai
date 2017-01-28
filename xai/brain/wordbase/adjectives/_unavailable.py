

#calss header
class _UNAVAILABLE():
	def __init__(self,): 
		self.name = "UNAVAILABLE"
		self.definitions = [u'If someone is unavailable, they are not able to talk to people or meet people, usually because they are doing other things: ', u'If something is unavailable, you cannot get it or use it: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
