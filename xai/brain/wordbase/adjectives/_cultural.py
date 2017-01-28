

#calss header
class _CULTURAL():
	def __init__(self,): 
		self.name = "CULTURAL"
		self.definitions = [u'relating to the habits, traditions, and beliefs of a society: ', u'relating to music, art, theatre, literature, etc.: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
