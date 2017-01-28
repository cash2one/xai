

#calss header
class _UNFAITHFUL():
	def __init__(self,): 
		self.name = "UNFAITHFUL"
		self.definitions = [u'having a sexual relationship or experience with a person who is not your husband, wife, or usual sexual partner: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
