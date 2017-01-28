

#calss header
class _PESSIMISTIC():
	def __init__(self,): 
		self.name = "PESSIMISTIC"
		self.definitions = [u'thinking that bad things are more likely to happen or emphasizing the bad part of a situation: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
