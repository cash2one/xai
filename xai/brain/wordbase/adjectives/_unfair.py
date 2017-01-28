

#calss header
class _UNFAIR():
	def __init__(self,): 
		self.name = "UNFAIR"
		self.definitions = [u'not treating people in an equal way, or not morally right: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
