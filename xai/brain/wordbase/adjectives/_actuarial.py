

#calss header
class _ACTUARIAL():
	def __init__(self,): 
		self.name = "ACTUARIAL"
		self.definitions = [u'relating to the work of an actuary, or to the job of being an actuary: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
