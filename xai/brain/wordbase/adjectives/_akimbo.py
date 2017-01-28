

#calss header
class _AKIMBO():
	def __init__(self,): 
		self.name = "AKIMBO"
		self.definitions = [u"If a person's arms are akimbo, they are bent at the elbows (= the middle part of the arms where they bend) with the hands on the hips: "]

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
