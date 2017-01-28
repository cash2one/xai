

#calss header
class _ORAL():
	def __init__(self,): 
		self.name = "ORAL"
		self.definitions = [u'spoken and not written: ', u'of, taken by, or done to the mouth: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
