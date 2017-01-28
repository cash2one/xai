

#calss header
class _PIGHEADED():
	def __init__(self,): 
		self.name = "PIGHEADED"
		self.definitions = [u'showing unreasonable support for an opinion or plan of action and refusing to change or listen to different opinions']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
