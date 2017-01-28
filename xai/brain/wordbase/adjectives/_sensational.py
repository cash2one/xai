

#calss header
class _SENSATIONAL():
	def __init__(self,): 
		self.name = "SENSATIONAL"
		self.definitions = [u'very good, exciting, or unusual: ', u'Sensational news reports and articles are intended to be shocking and exciting rather than serious: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
