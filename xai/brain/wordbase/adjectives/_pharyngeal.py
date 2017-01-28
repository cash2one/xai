

#calss header
class _PHARYNGEAL():
	def __init__(self,): 
		self.name = "PHARYNGEAL"
		self.definitions = [u'(of a speech sound) made by making the muscles in the pharynx tighter so that air cannot flow freely']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
