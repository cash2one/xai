

#calss header
class _HARDENED():
	def __init__(self,): 
		self.name = "HARDENED"
		self.definitions = [u'used to describe someone who has had a lot of bad experiences and as a result no longer gets upset or shocked: ', u'no longer likely to change a bad way of life or feel sorry about it: ', u'to develop a way of dealing with a sad situation so that it no longer upsets you: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
