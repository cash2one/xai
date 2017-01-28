

#calss header
class _SUPPLEMENTARY():
	def __init__(self,): 
		self.name = "SUPPLEMENTARY"
		self.definitions = [u'If an angle is supplementary to another angle, it forms 180\xb0 when combined with it.', u'extra: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
