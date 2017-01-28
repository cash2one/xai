

#calss header
class _UNEXPLORED():
	def __init__(self,): 
		self.name = "UNEXPLORED"
		self.definitions = [u'An unexplored place is one where people have not been to find out what is there: ', u'An unexplored plan, idea, or subject is one that has not been examined to find out what it involves: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
