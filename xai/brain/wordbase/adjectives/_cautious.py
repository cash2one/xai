

#calss header
class _CAUTIOUS():
	def __init__(self,): 
		self.name = "CAUTIOUS"
		self.definitions = [u'Someone who is cautious avoids risks: ', u'A cautious action is careful, well considered, and sometimes slow or uncertain: ', u'a feeling that there are some reasons to hope for a good result, even if you do not expect complete success or improvement']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
