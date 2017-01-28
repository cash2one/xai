

#calss header
class _PARAPLEGIC():
	def __init__(self,): 
		self.name = "PARAPLEGIC"
		self.definitions = [u'unable to move or feel the legs or lower part of the body: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
