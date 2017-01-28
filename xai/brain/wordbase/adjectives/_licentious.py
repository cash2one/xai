

#calss header
class _LICENTIOUS():
	def __init__(self,): 
		self.name = "LICENTIOUS"
		self.definitions = [u'(especially of a person or their behaviour) sexual in an uncontrolled and socially unacceptable way']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
