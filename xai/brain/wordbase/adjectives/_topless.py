

#calss header
class _TOPLESS():
	def __init__(self,): 
		self.name = "TOPLESS"
		self.definitions = [u'used to describe someone, usually a woman, wearing nothing on the upper part of the body, or something connected with this way of dressing: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
