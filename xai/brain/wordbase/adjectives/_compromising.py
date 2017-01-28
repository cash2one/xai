

#calss header
class _COMPROMISING():
	def __init__(self,): 
		self.name = "COMPROMISING"
		self.definitions = [u'causing damage to the reputation of someone, especially making known that they have had a sexual relationship with someone who is considered unsuitable: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
