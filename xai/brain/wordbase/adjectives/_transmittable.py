

#calss header
class _TRANSMITTABLE():
	def __init__(self,): 
		self.name = "TRANSMITTABLE"
		self.definitions = [u'able to be passed or sent from one person, thing, or place to another: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
