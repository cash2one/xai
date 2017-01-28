

#calss header
class _FURRED():
	def __init__(self,): 
		self.name = "FURRED"
		self.definitions = [u'A furred tongue is covered in a substance because of illness, smoking, etc.: ', u'Furred arteries (= tubes carry blood from your heart) that are slightly blocked: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
