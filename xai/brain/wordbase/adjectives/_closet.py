

#calss header
class _CLOSET():
	def __init__(self,): 
		self.name = "CLOSET"
		self.definitions = [u'used to refer to a belief, activity, or feeling that is kept secret from the public, usually because you are frightened of the results of it becoming known: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
