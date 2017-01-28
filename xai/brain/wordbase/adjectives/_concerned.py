

#calss header
class _CONCERNED():
	def __init__(self,): 
		self.name = "CONCERNED"
		self.definitions = [u'worried: ', u'involved in something or affected by it: ', u"in a particular person's opinion: ", u'if we are discussing or thinking about a particular thing: ', u'to be about a particular thing or person: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
