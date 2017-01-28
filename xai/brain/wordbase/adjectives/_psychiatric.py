

#calss header
class _PSYCHIATRIC():
	def __init__(self,): 
		self.name = "PSYCHIATRIC"
		self.definitions = [u'of or relating to the study of mental illness: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
