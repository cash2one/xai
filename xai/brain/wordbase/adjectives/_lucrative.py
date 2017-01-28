

#calss header
class _LUCRATIVE():
	def __init__(self,): 
		self.name = "LUCRATIVE"
		self.definitions = [u'(especially of a business, job, or activity) producing a lot of money: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
