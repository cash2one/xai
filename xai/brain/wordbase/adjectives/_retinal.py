

#calss header
class _RETINAL():
	def __init__(self,): 
		self.name = "RETINAL"
		self.definitions = [u'relating to the retina (= the area at the back of the eye that receives light): ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
