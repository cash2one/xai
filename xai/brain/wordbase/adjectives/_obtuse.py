

#calss header
class _OBTUSE():
	def __init__(self,): 
		self.name = "OBTUSE"
		self.definitions = [u'(of an angle) more than 90\xb0 and less than 180\xb0', u'stupid and slow to understand, or unwilling to try to understand: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
