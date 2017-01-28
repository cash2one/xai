

#calss header
class _EXTRINSIC():
	def __init__(self,): 
		self.name = "EXTRINSIC"
		self.definitions = [u'coming from outside, or not related to something: ', u'coming from outside the body: ', u'Extrinsic muscles are some distance from the body part they move: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
