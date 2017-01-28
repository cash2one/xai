

#calss header
class _PEAK():
	def __init__(self,): 
		self.name = "PEAK"
		self.definitions = [u'Peak times are the times when most people are using or doing something: ', u'Peak levels or rates are when they are at their highest: ', u'used to describe something that has become so popular and common that it is no longer fashionable or people start to dislike it: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
