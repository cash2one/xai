

#calss header
class _UNDERGROUND():
	def __init__(self,): 
		self.name = "UNDERGROUND"
		self.definitions = [u'below the surface of the earth; below ground: ', u'An underground activity is secret and usually illegal: ', u'a secret system, used in the 19th century, by which slaves (= people who had been sold and forced to work) in the southern US were helped to escape to places where there was no slavery']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
