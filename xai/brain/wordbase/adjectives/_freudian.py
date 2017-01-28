

#calss header
class _FREUDIAN():
	def __init__(self,): 
		self.name = "FREUDIAN"
		self.definitions = [u"relating to the ideas or methods of Sigmund Freud, especially his ideas about the way in which people's hidden thoughts and feelings influence their behaviour"]

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
